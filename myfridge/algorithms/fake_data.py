from faker import factory, Faker
from users.models import CustomUser, UserFollowing
from tools.models import ShoppingList, Meal, MealDailyPlan

fake = Faker()


def create_fake_user_data():
    num_users = CustomUser.objects.count()
    new_users = 50 - num_users
    user_list = []

    if new_users > 0:
        for _ in range(new_users):
            user = CustomUser(
                username=fake.user_name(),
                email=fake.email(),
                password=fake.password(),
                description=fake.text(max_nb_chars=200),
                newsletter=fake.boolean(),
            )
            user_list.append(user)

        CustomUser.objects.bulk_create(user_list)

    all_users = CustomUser.objects.all()

    for user in all_users:
        current_followings = UserFollowing.objects.filter(user_id=user).count()
        new_followings = 5 - current_followings
        following_list = []

        if new_followings > 0:
            for _ in range(new_followings):
                following = UserFollowing(
                    user_id=user,
                    following_user_id=fake.random_element(elements=all_users),
                )
                following_list.append(following)

            UserFollowing.objects.bulk_create(following_list)


def create_fake_shopping_list():
    num_shopping_lists = ShoppingList.objects.count()
    new_shopping_lists = 50 - num_shopping_lists
    shopping_list_list = []

    if new_shopping_lists > 0:
        for _ in range(new_shopping_lists):
            shopping_list = ShoppingList(
                name=fake.word(),
                author=fake.random_element(elements=CustomUser.objects.all()),
                quantity=fake.random_int(min=1, max=10),
                is_bought=fake.boolean(),
            )
            shopping_list_list.append(shopping_list)

        ShoppingList.objects.bulk_create(shopping_list_list)


def create_fake_meal():
    num_meals = Meal.objects.count()
    new_meals = 50 - num_meals
    meal_list = []
    num_daily_plan = MealDailyPlan.objects.count()
    new_daily_plan = 50 - num_daily_plan
    meal_daily_plan_list = []
    users = list(CustomUser.objects.all())
    meals = list(Meal.objects.all())

    if new_meals > 0:
        for _ in range(new_meals):
            meal = Meal(
                name=fake.word(),
                content=fake.text(max_nb_chars=200),
                user=fake.random_element(elements=CustomUser.objects.all()),
                url=fake.image_url(),
            )
            meal_list.append(meal)

        Meal.objects.bulk_create(meal_list)

        for _ in range(new_daily_plan):
            date = fake.date_between(start_date="-1y", end_date="today")
            month = date.strftime("%B")
            year = str(date.year)
            user = fake.random_element(users)
            breakfast = fake.random_element(meals)
            second_breakfast = fake.random_element(meals)
            lunch = fake.random_element(meals)
            tea = fake.random_element(meals)
            dinner = fake.random_element(meals)
            is_public = fake.boolean()

            meal_plan = MealDailyPlan(
                date=date,
                month=month,
                year=year,
                user=user,
                breakfast=breakfast,
                second_breakfast=second_breakfast,
                lunch=lunch,
                tea=tea,
                dinner=dinner,
                is_public=is_public,
            )

            meal_daily_plan_list.append(meal_plan)
        MealDailyPlan.bulk_create(meal_daily_plan_list)
