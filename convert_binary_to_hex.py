import os


BINARY_VALUES = []

file_path_input = input("Enter the path to the file containing 32-bit binary strings: ").strip('"')
file_path_input = file_path_input.strip('<>:"/\\|?*')
file_path_output = os.path.join(os.path.dirname(file_path_input), "hex_output.txt")
file_path_output_layout = os.path.join(os.path.dirname(file_path_input), "cfgspace_writemask_layout.txt")


def process_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            binary_string = line.strip()
            if len(binary_string) == 32 and all(c in '01' for c in binary_string):
                BINARY_VALUES.append(binary_string)
            else:
                print(f"Invalid input in file: {binary_string}")


def convert_binary_to_hex():
    hex_values = []
    layout_values = []

    for index, binary_string in enumerate(BINARY_VALUES, start=1):
        decimal_value = int(binary_string, 2)
        hexadecimal_conversion = hex(decimal_value)[2:].zfill(8)
        bytes_reversed = bytes.fromhex(hexadecimal_conversion)[::-1]
        converted_hex = bytes_reversed.hex()
        hex_values.append(f"{converted_hex}\n")
        layout_values.append(converted_hex)

    with open(file_path_output, 'w') as file_output:
        file_output.writelines(hex_values)

    with open(file_path_output_layout, 'w') as file_output_layout:
        for i in range(0, len(layout_values), 4):
            file_output_layout.write(','.join(layout_values[i:i+4]) + ',\n')


def main():
    process_file(file_path_input)
    convert_binary_to_hex()
    print(f"Converted {len(BINARY_VALUES)} binary strings to hexadecimal.")
    print(f"Saved to:\n{file_path_output}\n{file_path_output_layout}")

if __name__ == "__main__":
    main()