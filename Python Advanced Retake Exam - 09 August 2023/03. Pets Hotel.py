def accommodate_new_pets(available_capacity, max_weight_limit, *pets):
    accommodation = {}
    final_msg = []
    for pet_type, pet_weight in pets:
        if available_capacity <= 0:
            final_msg.append("You did not manage to accommodate all pets!")
            break
        if pet_weight > max_weight_limit:
            continue
        if pet_type not in accommodation:
            accommodation[pet_type] = 1
        else:
            accommodation[pet_type] += 1
        available_capacity -= 1
    else:
        final_msg.append(f"All pets are accommodated! Available capacity: {available_capacity}.")

    final_msg.append("Accommodated pets:")
    [final_msg.append(f'{pet_type}: {pet_count}') for pet_type, pet_count in sorted(accommodation.items())]

    return "\n".join(final_msg)