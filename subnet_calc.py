from dataclasses import dataclass

import typer


@dataclass
class Subnet:
    name: str
    subnet_id: str = None
    mask: str = None
    first_ip: str = None
    last_ip: str = None
    broadcast: str = None

    def __str__(self):
        """Returns a string representation of the Subnet object"""
        return (
            f"Subnet Name: {self.name}\n"
            f"Subnet ID: {self.subnet_id}\n"
            f"Mask: {self.mask}\n"
            f"First IP: {self.first_ip}\n"
            f"Last IP: {self.last_ip}\n"
            f"Broadcast: {self.broadcast}\n"
        )


@dataclass
class MainNetwork:
    IP_ID: str
    IP_MASK: int
    hosts: dict[str, int]
    subnets: list[Subnet] = None

    def _sort_by_hosts(self):
        """Sorts the hosts dictionary by the number of hosts in descending order"""
        host_names = list(self.hosts.keys())
        host_names.sort(key=lambda x: self.hosts[x], reverse=True)
        sorted_hosts = {x: self.hosts[x] for x in host_names}
        return sorted_hosts

    def _get_decimal_mask(self, mask):
        """Converts the mask from CIDR notation to decimal notation"""
        decimal_mask = ""
        for i in range(4):
            if i < mask // 8:
                decimal_mask += "255."
            elif i == mask // 8:
                decimal_mask += str(256 - 2 ** (8 - mask % 8)) + "."
            else:
                decimal_mask += "0."
        return decimal_mask[:-1]

    def _get_mask_by_hosts(self, num_hosts):
        """Calculates the mask based on the number of hosts required"""
        return 32 - (num_hosts + 2 - 1).bit_length()

    def _num_to_ip(self, num):
        """Converts a number to an IP address string"""
        ip = ""
        for i in range(4):
            ip += str(num // 256 ** (3 - i)) + "."
            num %= 256 ** (3 - i)
        return ip[:-1]

    def _ip_to_num(self, ip):
        """Converts an IP address string to a number"""
        ip = ip.split(".")
        ip = [int(octet) for octet in ip]
        ip = ip[0] * 256**3 + ip[1] * 256**2 + ip[2] * 256 + ip[3]
        return ip

    def calculate_subnet_ips(self):
        """Calculates the subnet details for the main network"""
        self.subnets = []
        sorted_hosts = self._sort_by_hosts()
        ip = self.IP_ID
        for subnet in sorted_hosts:
            mask = self._get_mask_by_hosts(sorted_hosts[subnet])
            network_address = ip.split(".")
            curr_subnet = Subnet(subnet)
            curr_subnet.subnet_id = ".".join(network_address) + "/" + str(mask)
            curr_subnet.mask = self._get_decimal_mask(mask)
            curr_subnet.first_ip = self._num_to_ip(self._ip_to_num(".".join(network_address)) + 1)
            curr_subnet.last_ip = self._num_to_ip(
                self._ip_to_num(".".join(network_address)) + 2 ** (32 - mask) - 2
            )
            curr_subnet.broadcast = self._num_to_ip(
                self._ip_to_num(".".join(network_address)) + 2 ** (32 - mask) - 1
            )
            ip = self._num_to_ip(self._ip_to_num(".".join(network_address)) + 2 ** (32 - mask))
            self.subnets.append(curr_subnet)

    def __repr__(self):
        """Returns a string representation of the MainNetwork object"""
        return (
            f"IP={self.IP_ID}/{str(self.IP_MASK)}\n"
            + "---------\n"
            + "\n".join([str(subnet) for subnet in self.subnets])
        )


def app(network_ip_cidr: str, hosts: list[str]):
    """
    Calculates the subnet details for the main network.
    Args:
        network_ip_cidr (str): The IP address of the main network in CIDR notation.
        hosts (list[str]): A list of the names of the subnets and the number of hosts required in each subnet.
    """
    IP_ID, IP_MASK = network_ip_cidr.split("/")
    hosts = {name: int(count) for name, count in [host.split("=") for host in hosts]}
    main_network = MainNetwork(IP_ID, IP_MASK, hosts)
    main_network.calculate_subnet_ips()
    print(main_network)


if __name__ == "__main__":
    typer.run(app)
