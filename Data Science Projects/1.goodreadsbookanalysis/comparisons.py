# Import necessary libraries
import os
from PIL import Image, ImageDraw, ImageFont

# -------------------------------
# Configuration
# -------------------------------
TITLES = [
    "Distribution of Average Ratings",
    "Top 20 Most Rated Books",
    "Top 20 Highest Rated Books (with >50K Ratings)",
    "Number of Ratings vs. Average Rating",
    "Distribution of Number of Ratings",
    "Top 10 Most Frequent Authors"
]

PYTHON_DIR = "screenshots/python/"
POWERBI_DIR = "screenshots/powerbi/"
OUTPUT_DIR = "screenshots/comparisons/"
FINAL_PDF_PATH = "screenshots/python_vs_powerbi_comparison.pdf"

# -------------------------------
# Helper Functions
# -------------------------------

def ensure_output_folder(path):
    os.makedirs(path, exist_ok=True)

def load_and_resize_images(python_path, powerbi_path, target_height):
    py_img = Image.open(python_path)
    pb_img = Image.open(powerbi_path)

    py_resized = py_img.resize((int(py_img.width * target_height / py_img.height), target_height))
    pb_resized = pb_img.resize((int(pb_img.width * target_height / pb_img.height), target_height))

    return py_resized, pb_resized

def add_title(draw_obj, title, padding=10, font_size=24):
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    draw_obj.text((padding, padding), title, fill="black", font=font)

def create_side_by_side(py_img, pb_img, title):
    spacing = 60
    total_width = py_img.width + pb_img.width
    total_height = py_img.height + spacing

    combined = Image.new("RGB", (total_width, total_height), color="white")
    draw = ImageDraw.Draw(combined)

    add_title(draw, title + " — Python (left) vs Power BI (right)")
    combined.paste(py_img, (0, spacing))
    combined.paste(pb_img, (py_img.width, spacing))

    return combined

# -------------------------------
# Main Function
# -------------------------------

def generate_comparisons():
    ensure_output_folder(OUTPUT_DIR)
    comparison_images = []

    for i in range(6):
        idx = i + 1
        title = TITLES[i]

        python_path = os.path.join(PYTHON_DIR, f"python_0{idx}.png")
        powerbi_path = os.path.join(POWERBI_DIR, f"powerbi_0{idx}.png")
        output_image_path = os.path.join(OUTPUT_DIR, f"comparison_0{idx}.png")

        # Load and resize
        py_img, pb_img = load_and_resize_images(python_path, powerbi_path, target_height=600)

        # Combine and save
        combined = create_side_by_side(py_img, pb_img, title)
        combined.save(output_image_path)
        comparison_images.append(combined)

    # Export to PDF
    comparison_images[0].save(
        FINAL_PDF_PATH,
        "PDF",
        resolution=100.0,
        save_all=True,
        append_images=comparison_images[1:]
    )

    print(f"\n✅ Comparison PNGs saved to: {OUTPUT_DIR}")
    print(f"📄 Final PDF exported to: {FINAL_PDF_PATH}\n")

# -------------------------------
# Entry Point
# -------------------------------

if __name__ == "__main__":
    generate_comparisons()
