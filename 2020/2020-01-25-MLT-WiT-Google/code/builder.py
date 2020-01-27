#########################################
# Builder
#########################################

query = "SELECT " + t1_col1 + "," + t1_col2 + "," +
    t2_col1 + " FROM " + t1_name  + " JOIN " +
    t2_name + " ON (" + t1_idcol + " = " + t2_idcol +
    ") ORDER BY " + t1_col1;

query = "SELECT {},{},{} FROM {} JOIN {} ON ({} = {}) ORDER BY {}" \
    .format(t1_col1, t1_col2, t2_col1, t1_name,
        t2_name, t1_idcol, t2_idcol,  t1_col1)

query = QueryBuilder(t1_name)
        .columns(t1_col1, t1_col2, t2_col1)
        .join(t2_name, t1_idcol, t2_idcol)
        .order_by(t1_col1)
        .build()


class QueryBuilder:

    def __init__(self, table):
        self.table = table
        self.cols = []
        self.joins = []
        self.orderbys = []

    def columns(self, *args):
        self.cols = ','.join(args)
        return self

    def join(self, other_table, col, other_col):
        self.joins.append('JOIN {} ON {}={}'.format(other_table, col, other_col))
        return self

    def order_by(col):
        self.orderbys.append(col)
        return self

    def build():
        # validation
        if not self.cols:
            raise Exception('Must specify columns')
        self.cols = unique(self.cols)

        # build
        q  = 'SELECT {} '.format(','.join(self.columns))
        q += 'FROM {} '.format(self.table)
        if self.joins:
            q += '{} '.format(' '.join(self.joins))
        if self.orderbys:
            q += ' ORDER BY {} '.format(','.join(self.orderbys))
        return q


query = QueryBuilder(t1_name)
        .columns(t1_col1, t1_col2, t2_col1)
        .join(t2_name, t1_idcol, t2_idcol)
        .order_by(t1_col1)
        .where(t1_col1, value1)
        .where(t2_col2, value2)
        .join(t3_name, t1_idcol, t3_idcol)
        .build()
