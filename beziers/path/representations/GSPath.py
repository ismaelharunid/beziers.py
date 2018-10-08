from beziers.path.representations.Nodelist import Node

class GSPathRepresentation(object):
  def __init__(self, path, gspath = None):
    self.nodes = []
    from beziers.path import BezierPath
    assert isinstance(path, BezierPath)
    self.path = path
    if (gspath):
      self.nodes = gspath.nodes
      self.closed = gspath.closed

  def toNodelist(self):
    return map( lambda n: Node(n.x,n.y,n.type), self.nodes)