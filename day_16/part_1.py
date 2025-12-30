import platform, sys, os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_path = '..' if platform.python_implementation() == 'CPython' else '.'

with open(base_path + '/inputs/real/input_day_16.txt', 'r') as file:
    input_lines = [i.rstrip("\n") for i in file.readlines()]

sample_lines = dict()
for x in range(1, 8, 1):
    with open(base_path + f'/inputs/sample/sample_input_day_16_{x}.txt', 'r') as file:
        sample_lines[x] = [i.rstrip("\n") for i in file.readlines()]

binary_dict = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}


def to_binary(hex):
    return ''.join([binary_dict[i] for i in hex])


def extract_literal(binary: str):
    vals = []
    while binary.startswith('1'):
        vals.append(binary[1:5])
        binary = binary[5:]

    vals.append(binary[1:5])
    binary = binary[5:]

    val = int(''.join(vals), 2)

    return val, binary


def get_packet_info(binary):
    version = int(binary[:3], 2)
    id = int(binary[3:6], 2)
    return version, id, binary[6:]


def extract_packet(binary: str):
    if len(binary) < 6:
        return None, ""

    version, id, binary = get_packet_info(binary)
    if id == 4:
        val, binary = extract_literal(binary)
        return (str(version), str(id), val), binary
    else:
        packets, binary = extract_operator(binary)
        return (str(version), str(id), packets), binary


def extract_operator(binary: str):
    if binary.startswith('0'):
        bit_length = int(binary[1:16], 2)
        binary_subpackets = binary[16:16 + bit_length + 1]
        binary_rest = binary[16 + bit_length:]

        packets = []
        while binary_subpackets:
            packet, binary_subpackets = extract_packet(binary_subpackets)
            if packet:
                packets.append(packet)

        return packets, binary_rest

    if binary.startswith('1'):
        packet_count = int(binary[1:12], 2)
        binary_rest = binary[12:]
        subpackets = []
        for i in range(packet_count):
            packet, binary_rest = extract_packet(binary_rest)
            subpackets.append(packet)
        return subpackets, binary_rest


def extract_versions(packets):
    version, id, packet = packets
    if id == '4':
        return int(version)
    else:
        return int(version) + sum([extract_versions(p) for p in packet])


def process(lines):
    hex = lines[0]
    binary = to_binary(hex)
    packets = extract_packet(binary)[0]
    versions = extract_versions(packets)
    return versions


for i, sample_line in sample_lines.items():
    print(f"Sample output {i}:", process(sample_line))
print("Answer:", process(input_lines))

# pypy ./day_16/part_1.py
