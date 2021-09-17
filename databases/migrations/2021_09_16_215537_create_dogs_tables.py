"""CreateDogsTables Migration."""

from masoniteorm.migrations import Migration


class CreateDogsTables(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("dogs") as table:
            table.increments("id")
            table.timestamps()
            table.string("name")
            table.integer("age")

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("dogs")
