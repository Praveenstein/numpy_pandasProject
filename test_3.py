x_pixel_mapping = {x_min: x_range[0]}
previous_value = x_pixel_mapping[x_min]
for x_pixel in range(x_min - 1, -1, -1):
    current_value = previous_value - x_factor
    x_pixel_mapping[x_pixel] = current_value
    previous_value = current_value