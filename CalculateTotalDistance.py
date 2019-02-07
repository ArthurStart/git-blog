file = '_posts/touring/2018-04-06-Progress-Updates.md'

print "Welcome to CalculateTotalDistance. Here to save you time, so you can get back to nature and away from the screen."

start = int(raw_input("Enter initial day number: "))
stop = int(raw_input("Enter final day number: "))

with open(file) as f:
    whole_thing = f.readlines()
    interesting_lines = [l for l in whole_thing if l[0] is '|']

    riding_days = []
    for l in interesting_lines:
        l = l.replace(' ', '').split('|')

        try:
            if int(l[1]) > 0 and int(l[-2]) > 0:
                riding_days.append([int(l[1]), int(l[-2])])
        except ValueError:
            pass

    riding_days.sort()
    included_days = [d for d in riding_days if start <= d[0] <= stop]

    for d in included_days:
        print 'Day:', d[0], 'Distance:', d[1], 'km.'
    sum = sum([d[1] for d in included_days])

    # sum += int(l[-2])

    print '\nTotal distance:', sum, 'km.\n'
