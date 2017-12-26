input_file= open ("input.txt")
i=0
for line in input_file:
    i=i+1
    print "#### %s ![big ]({{ site.img_path }}/slide/hanzi/%02d.png)\n\n---\n" % (line, i)
