def main(a):
    """
    If the number is positive, increase it to 1,otherwise leave unchanged.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else unchanged.
    """
    a=5
    f=if a>0:
        print(a+1)
    g=if a<0:
        print(a)
    return(f or g )

