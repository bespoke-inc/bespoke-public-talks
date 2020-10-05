#########################################
# Unit test
#########################################

class QueryBuilderTest(unittest.TestCase):

    def test_build_with_no_joins_or_orderbys(self):
        # GIVEN
        builder = QueryBuilder('foo_table')
                  .columns('bar')

        # WHEN
        query = builder.build()

        # THEN
        self.assertEqual(query, 'SELECT bar FROM foo_table')


    def test_build_with_joins_and_orderbys(self):
        # GIVEN
        builder = QueryBuilder('foo_table')
                  .columns('bar', 'baz')
                  .join('foo2', 'bar2', 'baz2')
                  .join('foo3', 'bar3', 'baz3')
                  .order_by('bar4')

        ...

