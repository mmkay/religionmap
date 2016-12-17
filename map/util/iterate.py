import itertools


def seq(start, end, step):
    assert (step != 0)
    sample_count = abs(end - start) / step
    return itertools.islice(itertools.count(start, step), sample_count)
