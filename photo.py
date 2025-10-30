from PIL import Image

# Open your uploaded image
img = Image.open("public2.png")

# Get image dimensions
width, height = img.size

# Define number of rows and columns
rows, cols = 2, 4
tile_width = width // cols
tile_height = height // rows

# Define file labels
labels = [
    "Primary_Care",
    "Pediatrics",
    "Immunizations",
    "Dental",
    "Sexual_Health",
    "Teen_Health",
    "Patient_Information",
    "Health_Centers_Health_Library"
]

# Crop and save each image
for i, label in enumerate(labels):
    col = i % cols
    row = i // cols
    left = col * tile_width
    upper = row * tile_height
    right = left + tile_width
    lower = upper + tile_height

    cropped = img.crop((left, upper, right, lower))
    cropped.save(f"{label}.png")

print("All images have been saved as separate PNG files.")
