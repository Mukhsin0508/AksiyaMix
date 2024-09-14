from django.shortcuts import render

from django.db import transaction
from apps.discount.models import Discount
from apps.branch.models import Branch

class DiscountMigrator:
    def __init__(self, branch_id, migrate=True):
        self.branch_id = branch_id
        self.migrate = migrate

    def migrate_discounts_to_company(self):
        """
        Migrate discounts from branch to company if migrate is True, otherwise delete discounts from branch
        :param branch_id: id of the branch
        :param migrate: True or False
        :return: none

        -> Note: transaction.atomic() is used to ensure that the operations of migrating or deleting discounts
        and then deleting the branch are treated as a single "transaction".
        If any part of this process fails, none of the changes will be committed to the database.
        """
        try:
            branch = Branch.objects.get(id=self.branch_id)
            company = branch.company

            with transaction.atomic():
                if self.migrate:
                    discounts = Discount.objects.filter(branch=branch).update(company=company, branch=None)
                    print(f"Discounts from branch {self.branch_id} "
                          f"have been successfully migrated to company {company.id}")
                else:
                    Discount.objects.filter(branch=branch).delete()
                    print(f"Discounts from branch {self.branch_id} have been successfully deleted")

            branch.delete()
            print(f"Branch with id {self.branch_id} has been successfully deleted")

        except Branch.DoesNotExist:
            print(f"Branch with id {self.branch_id} does not exist")

