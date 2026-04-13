# SDN Packet Logger using POX Controller
# Author: Sriranga Bharadwaj
# This controller captures and logs packets (Ethernet, IP, TCP, UDP, ICMP)
# and installs flow rules (match-action) in the switch.
# =========================================================

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4, tcp, udp, icmp

log = core.getLogger()


def _handle_PacketIn(event):
    """
    Handles PacketIn events from the switch.
    Logs packet details and installs flow rules.
    """
    packet = event.parsed

    if not packet.parsed:
        log.warning("Ignoring incomplete packet")
        return

    log.info("Packet Received")

    # Extract protocol layers
    eth = packet.find('ethernet')
    ip = packet.find('ipv4')
    tcp_pkt = packet.find('tcp')
    udp_pkt = packet.find('udp')
    icmp_pkt = packet.find('icmp')

    # -------------------------------
    # Ethernet Information
    # -------------------------------
    if eth:
        log.info(f"Ethernet: {eth.src} -> {eth.dst}")

    # -------------------------------
    # IPv4 Information
    # -------------------------------
    if ip:
        log.info(f"IPv4: {ip.srcip} -> {ip.dstip}")

    # -------------------------------
    # Protocol Detection
    # -------------------------------
    if tcp_pkt:
        log.info("Protocol: TCP")
    elif udp_pkt:
        log.info("Protocol: UDP")
    elif icmp_pkt:
        log.info("Protocol: ICMP (Ping)")
    else:
        log.info("Protocol: Other")

    # =====================================================
    #  FLOW RULE (Match-Action)
    # =====================================================
    flow_mod = of.ofp_flow_mod()
    flow_mod.match = of.ofp_match.from_packet(packet)

    # Action: Flood packet to all ports
    flow_mod.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

    event.connection.send(flow_mod)

    # =====================================================
    #  Forward current packet
    # =====================================================
    packet_out = of.ofp_packet_out()
    packet_out.data = event.ofp
    packet_out.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))

    event.connection.send(packet_out)


def launch():
    """
    Starts the POX controller module.
    """
    log.info(" Packet Logger Controller Started")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
