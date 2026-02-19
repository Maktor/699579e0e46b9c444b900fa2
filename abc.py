import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_pattern():
    # Increased figure size
    fig, ax = plt.subplots(figsize=(8, 8))

    # Expanded limits to accommodate the new boxes
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 8)

    # Original boxes
    ax.add_patch(patches.Rectangle((0, 0), 1, 5, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((1, 4), 4, 1, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((1, 3), 3, 1, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((1, 2), 3, 1, facecolor='blue', edgecolor='orange', lw=5))

    ax.add_patch(patches.Rectangle((3, 2), 1, 3, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((4, 2), 1, 3, facecolor='blue', edgecolor='orange', lw=5))

    ax.add_patch(patches.Rectangle((0, 1), 4, 1, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((0, 0), 4, 1, facecolor='blue', edgecolor='orange', lw=5))

    ax.add_patch(patches.Rectangle((4, 0), 1, 5, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((3, 0), 1, 2, facecolor='blue', edgecolor='orange', lw=5))

    # New boxes extending the pattern to an 8x8 grid
    ax.add_patch(patches.Rectangle((5, 0), 3, 2, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((5, 2), 1, 3, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((6, 2), 2, 1, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((6, 3), 2, 2, facecolor='blue', edgecolor='orange', lw=5))
    
    ax.add_patch(patches.Rectangle((0, 5), 2, 3, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((2, 5), 3, 1, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((5, 5), 3, 1, facecolor='blue', edgecolor='orange', lw=5))
    
    ax.add_patch(patches.Rectangle((2, 6), 1, 2, facecolor='blue', edgecolor='orange', lw=5))
    ax.add_patch(patches.Rectangle((3, 6), 5, 2, facecolor='blue', edgecolor='orange', lw=5))

    plt.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

draw_pattern()
