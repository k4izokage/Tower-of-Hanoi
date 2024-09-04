def print_towers(towers):
    """Print the current state of the towers."""
    max_height = max(len(tower) for tower in towers)
    for i in range(max_height-1, -1, -1):
        row = []
        for tower in towers:
            row.append(str(tower[i] if i < len(tower) else ' '))
        print(' | '.join(row))
    print('-' * (4 * len(towers) - 1))


def is_valid_move(towers, from_pole, to_pole):
    """Check if a move is valid."""
    if not towers[from_pole]:
        return False
    if not towers[to_pole] or towers[to_pole][-1] > towers[from_pole][-1]:
        return True
    return False


def move_disk(towers, from_pole, to_pole):
    """Move the top disk from one pole to another."""
    disk = towers[from_pole].pop()
    towers[to_pole].append(disk)


def main():
    n = int(input("Enter the number of disks: "))
    towers = [list(range(n, 0, -1)), [], []]
    
    print("Initial state:")
    print_towers(towers)
    
    while True:
        print("Current state:")
        print_towers(towers)
        
        from_pole = int(input("Move from (1, 2, or 3): ")) - 1
        to_pole = int(input("Move to (1, 2, or 3): ")) - 1
        
        if from_pole not in range(3) or to_pole not in range(3):
            print("Invalid pole. Choose between 1, 2, or 3.")
            continue
        
        if is_valid_move(towers, from_pole, to_pole):
            move_disk(towers, from_pole, to_pole)
        else:
            print("Invalid move. Make sure the disk you're moving is smaller than the one below it.")
            continue
        
        # Check for win condition
        if len(towers[2]) == n:
            print("Congratulations! You won!")
            break

if __name__ == "__main__":
    main()
