import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 12))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# Function to create a box with rounded edges
def create_box(ax, text, xy, width=9, height=1.5, fontsize=12, facecolor="#e1e1e1"):
    box = FancyBboxPatch(xy, width, height, boxstyle="round,pad=0.3", linewidth=2,
                         edgecolor="#4f4f4f", facecolor=facecolor)
    ax.add_patch(box)
    ax.text(xy[0] + width / 2, xy[1] + height / 2, text, ha="center", va="center", fontsize=fontsize, color="#333333")

# Adding connection arrows and labels
def add_arrow_with_label(ax, start, end, label):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", color="black", lw=1.5))
    # Adding the label horizontally beside the arrow
    mid_x = (start[0] + end[0]) / 2
    mid_y = (start[1] + end[1]) / 2
    ax.text(mid_x, mid_y, label, ha="center", va="center", fontsize=10, color="black")

# Define layers with descriptions and colors
layers = [
    ("Frontend / User Interface", "Web browser or application to visualize predictions or results.", "#b3d9ff"),
    ("Application Server Layer", "API Server on Django/Node.js, optional Docker for deployment.", "#ffcc99"),
    ("Processing Layer", "Machine Learning Server with linear regression model on CSV data.", "#ffb3b3"),
    ("Network and Security Layer", "Firewall and API Gateway for secure API access.", "#d9ffb3"),
    ("Cloud Storage Layer", "Cloud storage bucket for historical CSV versions or results.", "#c6b3ff")
]

# Positions of arrows with labels between layers
arrows = [
    ("HTTP Requests", (5, 11.8), (5, 10.2)),
    ("REST API Calls", (5, 9.3), (5, 6.1)),
    ("Model Inference", (5, 6.8), (5, 3.2)),
    ("Secure Data Storage", (5, 4.3), (5, 1.7))
]

# Draw each layer box and separate for arrow placements
y_position = 12  # Starting y position for the top layer
spacing = 1.5  # Space between boxes for arrows

for layer_name, description, color in layers:
    create_box(ax, f"{layer_name}\n{description}", (0.5, y_position), facecolor=color)
    y_position -= (2 + spacing)  # Adjust for next box position

# Draw arrows with labels
for label, start, end in arrows:
    add_arrow_with_label(ax, start, end, label)

# Display the final diagram
plt.show()
