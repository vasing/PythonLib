#!/usr/bin/env python3

"""
Timing your scripts
"""
import time

if __name__ == "__main__":
    start = time.time()
    a = range(100_000_00)
    b = []
    for i in a:
        b.append(i*2)
    end = time.time()
    print("The script took", f"{end - start:.3f}", "seconds to complete")      
