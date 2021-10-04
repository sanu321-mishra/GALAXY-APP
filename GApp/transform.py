def transform(self, x, y):
    #return self.transform_2D(x, y)
    return self.transform_perspective(x, y)


def transform_2D(self, x, y):
    return x, y


def transform_perspective(self, x, y):
    tr_y = y * self.perspective_point_y / self.height
    if tr_y > self.perspective_point_y:
        tr_y = self.perspective_point_y

    diff_x = x - self.perspective_point_x
    diff_y = self.perspective_point_y - tr_y
    proportion_y = diff_y / self.perspective_point_y  # 1 when diff_y==self.percpective_point_y/0 when diff 1==0
    tr_x = self.perspective_point_x + diff_x * proportion_y

    return int(tr_x), int(tr_y)