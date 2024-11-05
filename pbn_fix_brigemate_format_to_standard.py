"""
##############################################################################
# Script Name:       pbn_fix_brigemate_format_to_standard.py
# Author:            jarek7410
# Email:             jarekomsta+brige@gmail.com
# Created Date:      2024.11.05
# Last Modified:     2024.11.05
# Description:       This script copies specific lines from an input file to
#                    an output file based on a repeating line pattern within
#                    blocks of lines.
#
# Usage:
#   python copy_patterned_lines.py <inputfile> <outputfile>
#
# Arguments:
#   <inputfile>      Path to the input file to process.
#   <outputfile>     Path to the output file where results are saved.
#
# Example:
#   python copy_patterned_lines.py input.pbn output.pbn
#
# Notes:
#   - Modify the `line_pattern` variable in the script to customize which
#     line numbers to copy within each 40-line block.
#   - Ensure that both the input file and output file paths are accessible.
#
# License:           [MIT]
#
##############################################################################
"""
import sys
import argparse


def load_file_and_copy_patterned_lines(filename, line_pattern, output_filename):
    """
    Load a file and copy lines based on a repeating line number pattern.

    Args:
        filename (str): The path to the input file.
        line_pattern (list): A list of line numbers (1-based within each block) to copy in a repeated pattern.
        output_filename (str): The path for the output file where lines will be copied.
    """
    try:
        with open(filename, 'r') as file:
            all_lines = file.readlines()  # Read all lines from the file

        matching_lines = []

        # Go through each block of lines based on the pattern length
        for i in range(0, len(all_lines), max(line_pattern)):
            for line_number in line_pattern:
                target_index = i + line_number - 1  # Calculate the actual line index in the file
                if target_index < len(all_lines):
                    matching_lines.append(all_lines[target_index])
                else:
                    print(f"Reached end of file before completing pattern at block starting line {i + 1}.")
                    break

        # Write the matched lines to the output file
        with open(output_filename, 'w') as output_file:
            output_file.writelines(matching_lines)

        print(f"Patterned lines {line_pattern} were written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     # Example usage:
#     # Define the input file, line pattern, and output file
#     filename = "241015.pbn"  # Replace with your file path
#     line_pattern = [1,2,3,4,9,10,11,40]  # Repeating pattern of line numbers within each block
#     output_filename = "output.pbn"  # Name of the file to store the output
#     load_file_and_copy_patterned_lines(filename, line_pattern, output_filename)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Copy specific lines from input file to output file based on a repeating line pattern."
                    "it changes pbn file format from brigemate format to one used by Turnament calculator and dealer4")
    parser.add_argument("inputfile", help="Path to the input file")
    parser.add_argument("outputfile", help="Path to the output file")

    args = parser.parse_args()

    # Define the line pattern within each 40-line block
    line_pattern = {1, 2, 3, 4, 9, 10, 11, 40}  # Set of line numbers to capture within each 40-line block

    # Run the function with the provided arguments
    load_file_and_copy_patterned_lines(args.inputfile, line_pattern, args.outputfile)
