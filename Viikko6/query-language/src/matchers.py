class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class Not:
  def __init__(self, *matchers):
    self._matchers = matchers

  def matches(self, player):
    for matcher in self._matchers:
      if matcher.matches(player):
        return False
    return True

class Or:
  def __init__(self, *matchers):
    self._matchers = matchers

  def matches(self, player):
    counter = 0
    for matcher in self._matchers:
      if matcher.matches(player):
        counter =+1
    if counter > 0:
      return True
    return False

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self):
      pass

    def matches(self,player):
      return True


class HasFewerThan:
    def __init__(self, value, attr):
      self._value = value
      self._attr = attr

    def matches (self,player):
      player_value = getattr(player, self._attr)

      return player_value < self._value

class QueryBuilder:
  def __init__(self, mathcer_object = All()):
    self._matcher_object = mathcer_object

  def build(self):
    return self._matcher_object

  def playsIn(self,attr):
    return QueryBuilder(And(PlaysIn(attr), self._matcher_object))
    
  def hasAtLeast(self, value, attr):
    return QueryBuilder(And(HasAtLeast(value, attr), self._matcher_object))

  def hasFewerThan(self, value, attr):
    return QueryBuilder(And(HasFewerThan(value, attr), self._matcher_object))

  def oneOf(self, matcher1, matcher2):
    return QueryBuilder(Or(matcher1, matcher2))