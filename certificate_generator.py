from PIL import Image, ImageDraw, ImageFont


# Path to your template image
template_path = "path_to_template_certificate" 

# Path to folder to store generated certificates
output_path = "path_to_output_folder"    

# Play around with "font_path", "font_size" and "name_position" to match the template
# Path to your font file (eg: Arial.ttf)
font_path = "font.ttf"   

# Font Size
font_size = 120 

# (x, y) position to place the name
name_position = (800, 600)                  

def generate_certificate(name):
    try:
        template = Image.open(template_path)
        draw = ImageDraw.Draw(template)

        font = ImageFont.truetype(font_path, font_size)

        draw.text(name_position, name, fill="black", font=font)

        template.save(f"{output_path}/{name}.png")
        print(f"Certificate saved: {output_path}")

    except Exception as e:
        print(f"Error generating certificate: {e}")

# Uncomment the following line to see test the certificate preview
# generate_certificate("Testing", template_path, "testing.png", font_path, font_size, name_position)

# Uncomment the following lines to generate certificates for the people
"""
# Names of people for generating certificate, you can also use pandas and create list of names
names = []

for _ in names:
    generate_certificate(_)

"""