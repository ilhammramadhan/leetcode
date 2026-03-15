class Fancy:
    def __init__(self):
        self.seq = []
        self.add = 0
        self.mult = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        # We need to reverse the current global transformations so that 
        # when they are applied later, the value comes out as 'val'.
        # Formula: (val - add) / mult
        # Under modulo, division by mult is multiplication by modular inverse of mult.
        
        mod_inv_mult = pow(self.mult, self.MOD - 2, self.MOD)
        base_val = ((val - self.add) * mod_inv_mult) % self.MOD
        self.seq.append(base_val)

    def addAll(self, inc: int) -> None:
        # Increase the global addition.
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        # Multiply both the global multiplier and the global addition.
        self.mult = (self.mult * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        # Check for out of bounds
        if idx >= len(self.seq):
            return -1
        
        # Re-apply the global transformations to the stored base value.
        # Formula: (stored_value * mult) + add
        actual_val = (self.seq[idx] * self.mult + self.add) % self.MOD
        return actual_val

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)