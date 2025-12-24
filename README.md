# Brute Force Login Detection - SOC Simulation
## Description

This project simulates a Security Operations Center (SOC) use case by detecting potential brute force attacks through authentication log analysis. The script parses Linux-style SSH logs, extracts source IP addresses using regular expressions, and correlates repeated failed login attempts to generate alerts based on a defined threshold.

## Key Objectives

-Simulate real-world SOC alert logic.

-Identify suspicious authentication behavior.

-Demonstrate log parsing and event correlation.

## How It Works

-Processes simulated SSH authentication logs (auth.log).

-Uses regex to extract IP addresses from failed login events.

-Counts repeated failures per IP using efficient data structures.

-Triggers alerts when activity exceeds a brute-force threshold.

## SOC & Security Concepts 

-Log analysis and alert triage.

-Brute force attack detection.

-Event correlation and threshold-based alerting.

-Secure handling of simulated log data. 

## MITRE ATT&CK Mapping

T1110 – Brute Force

## Technologies Used

-Python

-Regular Expressions (re)

-defaultdict for event counting

-Simulated Linux authentication logs
