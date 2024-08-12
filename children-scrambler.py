import os
import random

def get_children(path: str) -> list:
    children = os.listdir(path)
    
    # Make the python script an exception.
    try: 
        children.remove("children-scrambler.py")
    except ValueError: 
        pass
    return children
    
def scramble_children(path: str):
    children = get_children(path)
    
    if len(children) > 1:
        print(f"Scrambling {path}")
        
        new_children = children.copy()
        while children == new_children:
            random.shuffle(new_children)
        
        # Two loops are required to prevent errors with two folders using the 
        # same name.
        # The first loop shuffles and adds .temp suffix to prevent the issue.
        # The second loop removes the .temp suffix
        
        for i in range(len(children)):
            child_path = os.path.join(path, children[i])
            new_child_path = os.path.join(path, f"{new_children[i]}.temp")
            os.rename(child_path, new_child_path)
            print(f"Renamed {children[i]} to {new_children[i]}")
        
        for child in children:
            child_path = os.path.join(path, f"{child}.temp")
            new_child_path = os.path.join(path, child)
            os.rename(child_path, new_child_path)
    
    # Recusively scramble all directories found for maximum damage >:D
    for child in children:
        try:
            scramble_children(os.path.join(path, child))
        except NotADirectoryError:
            pass

print("Are you sure you want to run this script? This will cause damage to this directory.")
if input(f"Type out `{os.getcwd()}` to confirm: ") == os.getcwd():
    scramble_children(os.getcwd())
else:
    print("Cancelled")
