import sys

def foo():
    print("\n calling foo()....")
    aString = 'a'
    anInt = 24
    print("foo()'s globals:" , globals().keys())
    print("foo()'s locals" , locals().keys())

print (sys.version)
print (sys.version_info)

print ("__mains_'s global", globals().keys())
print ("__mains's locals" , locals().keys())
print ("__mains's locals" , locals().keys())