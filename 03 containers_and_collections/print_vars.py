# import builtins

# __package__ = "package1"
# __name__ = "name1"
# __doc__ = "doc1"
# __file__ = "file1"

def __main__():
    print "print from main..."


print "locals : %s" % locals()
print "globals : %s " % globals()

# __main__()

# print "builtin vars : ", vars(builtins)
