def draw_box_in_terminal(width, height, char='*'):
    if width < 2 or height < 2:
        print("Width and height must be at least 2.")
        return

    top_bottom = char * width
    middle = char + ' ' * (width - 2) + char

    print(top_bottom)
    for _ in range(height - 2):
        print(middle)
    print(top_bottom)

# Example usage:
draw_box_in_terminal(10, 4)
