# SDN Packet Logger using POX Controller

## 📌 Problem Statement

This project implements a Software Defined Networking (SDN) solution using Mininet and POX controller to capture and log packets traversing the network.

\---

## 🎯 Objectives

* Demonstrate controller–switch interaction
* Implement OpenFlow match-action rules
* Capture and log packet details
* Identify protocol types (ICMP, TCP, UDP)

\---

## 🛠️ Tools Used

* Mininet
* POX Controller
* OpenFlow Protocol
* iperf

\---

## ⚙️ Setup \& Execution

### Start Controller

```bash
cd \~/pox
./pox.py misc.packet\_logger# POX

POX is a networking software platform written in Python.

POX started life as an OpenFlow controller, but can now also function as an
OpenFlow switch, and can be useful for writing networking software in
general.  It currently supports OpenFlow 1.0 and includes special support
for the Open vSwitch/Nicira extensions.

POX versions are named.  Starting with POX "gar", POX officially requires
Python 3.  The last version with support for Python 2 was POX "fangtooth".
POX should run under Linux, Mac OS, and Windows.  (And just about anywhere
else -- we've run it on Android phones, under FreeBSD, Haiku, and elsewhere.
All you need is Python!)  Some features are not available on all platforms.
Linux is the most featureful.

This README contains some information to get you started, but is purposely
brief.  For more information, please see the full documentation.






