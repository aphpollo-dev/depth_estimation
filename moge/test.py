from concurrent.futures import ThreadPoolExecutor

x = 2

def blk1(x):
    return x**2

def blk2(x):
    return x+2

blks = [blk1, blk2]  # Ordered list of functions

# Define a helper function for applying a block
def apply_block(block, x):
    return block(x)

# Execute functions in parallel
with ThreadPoolExecutor() as executor:
    results = list(executor.map(apply_block, blks, [x] * len(blks)))

# Combine results if needed (e.g., summing them)
final_result = sum(results)

print(final_result)
