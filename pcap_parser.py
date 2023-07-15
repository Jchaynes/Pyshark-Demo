import argparse
import logging
import os
from collections import defaultdict
from ipaddress import IPv4Address, IPv6Address, ip_network

import pyshark


class PcapParser:
    def __init__(self, directory: str, output_file: str = "known_hosts.txt", extract_files: bool = False):
        self.directory = directory
        self.file_captures = []
        self.output_file = output_file
        self.ipv4_hosts = set()
        self.ipv6_hosts = set()
        self.host_interactions = defaultdict(set)
        self.logger = logging.getLogger("PcapParser")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def read_pcap_files(self, display_filter: str = "", print_files: bool = False) -> None:
        valid_extensions = (".pcap", ".pcapng", ".cap")

        for file_name in os.listdir(self.directory):
            if file_name.lower().endswith(valid_extensions):
                file_path = os.path.join(self.directory, file_name)
                capture = pyshark.FileCapture(file_path, display_filter=display_filter)
                self.file_captures.append(capture)
                self.logger.info(f"Found pcap file: {file_name} ({file_path})")

                if print_files:
                    self.print_files_in_capture(capture)

    def print_files_in_capture(self, capture):
        files = capture.file_names
        if files:
            self.logger.info("Files found in the packet capture:")
            for file in files:
                self.logger.info(file)

    def parse_pcap(self, ip_range: list[ip_network] = None, protocol: str = None) -> None:
        for capture in self.file_captures:
            for packet in capture:
                if 'ip' in packet:
                    source_ip = packet.ip.src
                    destination_ip = packet.ip.dst

                    if ip_range is not None and not self.is_ip_in_range(source_ip, ip_range) and not self.is_ip_in_range(destination_ip, ip_range):
                        continue

                    if protocol is not None and packet.layers[1].layer_name != protocol:
                        continue

                    if '.' in source_ip:
                        self.ipv4_hosts.add(source_ip)
                    else:
                        self.ipv6_hosts.add(source_ip)

                    if '.' in destination_ip:
                        self.ipv4_hosts.add(destination_ip)
                    else:
                        self.ipv6_hosts.add(destination_ip)

                    self.host_interactions[source_ip].add(destination_ip)
                    self.host_interactions[destination_ip].add(source_ip)

                if 'ipv6' in packet:
                    source_ip = packet.ipv6.src
                    destination_ip = packet.ipv6.dst

                    if ip_range is not None and not self.is_ip_in_range(source_ip, ip_range) and not self.is_ip_in_range(destination_ip, ip_range):
                        continue

                    if protocol is not None and packet.layers[1].layer_name != protocol:
                        continue

                    if ':' in source_ip:
                        self.ipv6_hosts.add(source_ip)
                    else:
                        self.ipv4_hosts.add(source_ip)

                    if ':' in destination_ip:
                        self.ipv6_hosts.add(destination_ip)
                    else:
                        self.ipv4_hosts.add(destination_ip)

                    self.host_interactions[source_ip].add(destination_ip)
                    self.host_interactions[destination_ip].add(source_ip)

        sorted_ipv4_hosts = sorted(self.ipv4_hosts, key=lambda ip: (ip_network(ip).network_address, ip))
        sorted_ipv6_hosts = sorted(self.ipv6_hosts, key=lambda ip: (ip_network(ip).network_address, ip))

        with open(self.output_file, "w") as file:
            file.write("Unique IPv4 Addresses:\n")
            for host in sorted_ipv4_hosts:
                file.write(f"{host}\n")
            file.write("\n")

            file.write("Unique IPv6 Addresses:\n")
            for host in sorted_ipv6_hosts:
                file.write(f"{host}\n")
            file.write("\n")

    def is_ip_in_range(self, ip: str, ip_range: list[ip_network]) -> bool:
        ip_address = IPv4Address(ip) if '.' in ip else IPv6Address(ip)
        for network in ip_range:
            if ip_address in network:
                return True
        return False

    def store_hosts_interactions(self, output_file: str = "host_interactions.csv") -> None:
        with open(output_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Source", "Interacted Hosts"])

            for host, interactions in self.host_interactions.items():
                writer.writerow([host, ", ".join(interactions)])

def main(pcap_directory: str, output_file: str = "known_hosts.txt"):
    pcap_parser = PcapParser(pcap_directory, output_file)

    # Read the pcap files from the directory
    pcap_parser.read_pcap_files()

    # Parse and process the pcap files
    pcap_parser.parse_pcap(ip_range=None, protocol=None)

    # Store the host interactions
    pcap_parser.store_hosts_interactions()
    pcap_parser

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PCAP Parser")
    parser.add_argument("pcap_directory", help="Path to the directory containing the PCAP files")
    parser.add_argument("--output_file", help="Path to the output file", default="known_hosts.txt")
    parser.add_argument("--extract-files", help="Extract files from the packet captures.", default=False)
    args = parser.parse_args()

    main(args.pcap_directory, args.output_file)
