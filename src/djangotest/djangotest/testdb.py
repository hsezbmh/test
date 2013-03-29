from polls.models import Poll,Choice

from django.utils import timezone

p = Poll.objects.get(pk=1)
p.choice_set.all()
p.choice_set.create(choice_text="Day",votes=0)
p.choice_set.create(choice_text="Night",votes=0)
c = p.choice_set.create(choice_text="Just want to see the result",votes=0)
print c.poll
print p.choice_set.all()
print p.choice_set.count()
