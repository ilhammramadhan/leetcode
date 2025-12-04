class Solution:
    def countCollisions(self, directions: str) -> int:
        # Step 1: Remove cars moving Left at the very beginning (safe cars)
        # lstrip('L') removes leading 'L' characters
        temp = directions.lstrip('L')
        
        # Step 2: Remove cars moving Right at the very end (safe cars)
        # rstrip('R') removes trailing 'R' characters
        collision_zone = temp.rstrip('R')
        
        # Step 3: Count collisions
        # In the collision zone, every car that is NOT 'S' will crash.
        # We calculate this by taking the total length and subtracting the 'S' cars.
        return len(collision_zone) - collision_zone.count('S')