import os
import subprocess

# Set input and output file paths

input_file = input("Enter the file path of the video you want to compress: ")
if "C:\\Users\\rchir\\Videos\\Captures\\" in input_file:
    output_file = input_file.replace(
        "C:\\Users\\rchir\\Videos\\Captures\\",
        "C:\\Users\\rchir\\Videos\\Captures\\Compressed\\",
    )
    if not os.path.exists("C:\\Users\\rchir\\Videos\\Captures\\Compressed\\"):
        os.makedirs("C:\\Users\\rchir\\Videos\\Captures\\Compressed\\")

output_file = "".join(output_file.split(".")[:1]) + "_compressed.mp4"
print(output_file)

assert os.path.exists(input_file), "File not found"
print(
    "Are you sure you want to compress this file? " + input_file + " [Y] or [N]: "
) or "Y"
if input().lower() == "n":
    exit()


# Set bitrate (in kbps)
bitrate = input("Enter the bitrate in Mb. Defaults to 10Mb: ") or "10Mb"
bitrate = str(int("".join(filter(str.isdigit, bitrate))) * 1000) + "k"

# Set resolution
resolution = (
    input("Enter the resolution. Eg: 1920x1080. Defaults to 1812x1080: ") or "1812x1080"
)
# resolution = (1812, 1080)

# Set frame rate
fps = "60"

# Get file size before compression
original_size = os.path.getsize(input_file)

# Run FFmpeg command
subprocess.run(
    [
        "ffmpeg",
        "-i",
        input_file,
        "-c:v",
        "libx264",
        "-b:v",
        bitrate,
        "-r",
        fps,
        "-s",
        resolution,
        output_file,
    ]
)

# Get file size after compression
compressed_size = os.path.getsize(output_file)

# write the new compressed size in Mb
print("Compressed file size: " + str(round(compressed_size / 1000000, 2)) + "MB")
print(output_file)
