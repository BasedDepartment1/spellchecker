import bisect


class Matcher(object):
    def __init__(self, base: list[str]):
        self.base = base
        base.sort()
        self.probes = 0

    def __call__(self, w) -> str | None:
        self.probes += 1
        pos = bisect.bisect_left(self.base, w)
        if pos < len(self.base):
            return self.base[pos]
        else:
            return None
