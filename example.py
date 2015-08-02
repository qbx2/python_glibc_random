#!/usr/bin/env python
import glibc_prng

prng = glibc_prng.glibc_prng(1)

for _ in range(10):
	print(next(prng))
