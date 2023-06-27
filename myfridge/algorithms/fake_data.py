from faker import factory, Faker
from users.models import CustomUser, UserFollowing
from tools.models import (
    ShoppingList,
    Meal,
    MealDailyPlan,
    CaloricNeedsStatistics,
    PerfectWeightStatistics,
    BmiStatistics,
)
from social.models import Rate, Feedback, FavouriteDish
from fak.models import Fak, Medicine
from dishes.models import (
    Type,
    Country,
    MainIngredient,
    OtherIngredient,
    DifficultyLevel,
    DishCategory,
    TimeToMake,
    Dish,
)
from blog.models import Post, Comment

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


def create_fake_daily_meal_plan():
    num_daily_plan = MealDailyPlan.objects.count()
    new_daily_plan = 50 - num_daily_plan
    meal_daily_plan_list = []
    users = list(CustomUser.objects.all())
    meals = list(Meal.objects.all())

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
    MealDailyPlan.objects.bulk_create(meal_daily_plan_list)


def create_fake_caloric_needs():
    num_caloric_needs = CaloricNeedsStatistics.objects.count()
    new_caloric_needs = 50 - num_caloric_needs
    caloric_needs_list = []

    for _ in range(new_caloric_needs):
        meal_plan = CaloricNeedsStatistics(
            weight=fake.random_int(min=50, max=100),
            height=fake.random_int(min=150, max=200),
            age=fake.random_int(min=18, max=80),
            gender=fake.random_element(elements=["Male", "Female"]),
            caloric_needs=fake.random_int(min=1000, max=4000),
            activity_level=fake.random_element(elements=["Low", "Medium", "High"]),
        )

        caloric_needs_list.append(meal_plan)
    CaloricNeedsStatistics.objects.bulk_create(caloric_needs_list)


def create_fake_perfect_weight():
    perfect_weight_num = PerfectWeightStatistics.objects.count()
    new_perfect_weight = 50 - perfect_weight_num
    perfect_weight_list = []

    for _ in range(new_perfect_weight):
        meal_plan = PerfectWeightStatistics(
            height=fake.random_int(min=150, max=200),
            min_perfect_weight=fake.random_int(min=50, max=100),
            max_perfect_weight=fake.random_int(min=50, max=150),
        )

        perfect_weight_list.append(meal_plan)
    PerfectWeightStatistics.objects.bulk_create(perfect_weight_list)


def create_fake_bmi():
    bmi_num = CaloricNeedsStatistics.objects.count()
    new_bmi = 50 - bmi_num
    bmi_list = []

    for _ in range(new_bmi):
        meal_plan = BmiStatistics(
            height=fake.random_int(min=150, max=200),
            weight=fake.random_int(min=50, max=120),
            bmi=fake.random_int(min=10, max=40),
        )

        bmi_list.append(meal_plan)
    BmiStatistics.objects.bulk_create(bmi_list)


def create_fake_feedback():
    feedback = Feedback.objects.count()
    new_feedback = 50 - feedback
    feedback_list = []

    for _ in range(new_feedback):
        feedback = Feedback(
            message=fake.text(max_nb_chars=150),
        )
        feedback_list.append(feedback)
    Feedback.objects.bulk_create(feedback_list)


def create_fake_fak():
    users = list(CustomUser.objects.all())
    fak_num = Fak.objects.count()
    new_fak = 50 - fak_num
    fak_list = []

    for _ in range(new_fak):
        fak = Fak(
            name=fake.words(),
            author=fake.random_element(elements=users),
        )
        fak_list.append(fak)
    Fak.objects.bulk_create(fak_list)


def create_fake_medicine():
    medicine_num = Medicine.objects.count()
    new_medicine = 50 - medicine_num
    medicine_list = []

    for _ in range(new_medicine):
        medicine = Medicine(
            name=fake.text(max_nb_chars=50),
            expieration_date=fake.date_between(start_date="today", end_date="+1y"),
            quantity=fake.random_element(elements=["LOW", "MEDIUM", "HIGH"]),
            fak=fake.random_element(elements=Fak.objects.all()),
            author=fake.random_element(elements=CustomUser.objects.all()),
        )
        medicine_list.append(medicine)
    Medicine.objects.bulk_create(medicine_list)


def create_fake_type():
    type_num = Type.objects.count()
    new_type = 50 - type_num
    type_list = []

    for _ in range(new_type):
        type = Type(
            name=fake.text(max_nb_chars=50),
        )
        type_list.append(type)
    Type.objects.bulk_create(type_list)


def create_fake_country():
    country_num = Type.objects.count()
    new_country = 50 - country_num
    country_list = []

    for _ in range(new_country):
        country = Country(
            name=fake.text(max_nb_chars=50),
        )
        country_list.append(country)
    Country.objects.bulk_create(country_list)


def create_fake_main_ingredient():
    main_ingredient = MainIngredient.objects.count()
    new_main_ingredient = 50 - main_ingredient
    main_ingredient_list = []

    for _ in range(new_main_ingredient):
        main_ingredient = MainIngredient(
            name=fake.text(max_nb_chars=50),
            type=fake.random_element(elements=Type.objects.all()),
        )
        main_ingredient_list.append(main_ingredient)
    MainIngredient.objects.bulk_create(main_ingredient_list)


def create_fake_other_ingredient():
    other_ingredient = OtherIngredient.objects.count()
    new_other_ingredient = 50 - other_ingredient
    other_ingredient_list = []

    for _ in range(new_other_ingredient):
        other_ingredient = OtherIngredient(
            name=fake.text(max_nb_chars=50),
            type=fake.random_element(elements=Type.objects.all()),
        )
        other_ingredient_list.append(other_ingredient)
    OtherIngredient.objects.bulk_create(other_ingredient_list)


def create_difficulty_leveL():
    level_num = DifficultyLevel.objects.count()
    new_level = 10 - level_num
    level_list = []

    for _ in range(new_level):
        level = DifficultyLevel(
            name=fake.text(max_nb_chars=50),
        )
        level_list.append(level)
    DifficultyLevel.objects.bulk_create(level_list)


def create_dish_category():
    category_num = DishCategory.objects.count()
    new_category = 10 - category_num
    category_list = []

    for _ in range(new_category):
        category = DishCategory(
            name=fake.text(max_nb_chars=50),
        )
        category_list.append(category)
    DishCategory.objects.bulk_create(category_list)


def create_fake_time_to_make():
    time_to_make = TimeToMake.objects.count()
    new_time_to_make = 50 - time_to_make
    time_to_make_list = []

    for _ in range(new_time_to_make):
        time_to_make = TimeToMake(value=fake.random_int(min=10, max=180))
        time_to_make_list.append(time_to_make)
    TimeToMake.objects.bulk_create(time_to_make_list)


def create_fake_dish():
    dish_num = Dish.objects.count()
    new_dish = 50 - dish_num
    dish_list = []

    for _ in range(new_dish):
        dish = Dish(
            name=fake.text(max_nb_chars=50),
            author=fake.random_element(elements=CustomUser.objects.all()),
            time_to_make=fake.random_element(elements=TimeToMake.objects.all()),
            description=fake.text(max_nb_chars=150),
            kcal=fake.random_int(min=100, max=1000),
            gluten=fake.boolean(),
            lactose=fake.boolean(),
            meat=fake.boolean(),
            vegetarian=fake.boolean(),
            vegan=fake.boolean(),
            country=fake.random_element(elements=Country.objects.all()),
            level=fake.random_element(elements=DifficultyLevel.objects.all()),
            category=fake.random_element(elements=DishCategory.objects.all()),
        )
        dish.save()
        dish.main_ingredient.add(
            fake.random_element(elements=MainIngredient.objects.all())
        )
        dish.other_ingredients.add(
            fake.random_element(elements=OtherIngredient.objects.all())
        )
        dish_list.append(dish)
    Dish.objects.bulk_create(dish_list)


def create_fake_rate():
    rate_num = Rate.objects.count()
    new_rate = 50 - rate_num
    rate_list = []
    dishes = list(Dish.objects.all())
    users = list(CustomUser.objects.all())

    for _ in range(new_rate):
        rate = Rate.objects.create(
            choose_rate=fake.random_int(min=1, max=5),
            dish=fake.random_element(elements=dishes),
            author=fake.random_element(elements=users),
            comment=fake.text(max_nb_chars=150),
        )
        rate_list.append(rate)
    Rate.objects.bulk_create(rate_list)


def create_fake_favourite_dish():
    fav_num = Rate.objects.count()
    new_fav = 50 - fav_num
    fav_list = []
    dishes = list(Dish.objects.all())
    users = list(CustomUser.objects.all())

    for _ in range(new_fav):
        rate = FavouriteDish.objects.create(
            dish=fake.random_element(elements=dishes),
            user=fake.random_element(elements=users),
        )
        fav_list.append(rate)
    Rate.objects.bulk_create(fav_list)


def create_fake_post():
    post_num = Post.objects.count()
    new_post = 50 - post_num
    post_list = []
    users = list(CustomUser.objects.all())

    for _ in range(new_post):
        post = Post.objects.create(
            title=fake.text(max_nb_chars=200),
            text=fake.text(max_nb_chars=150),
            author=fake.random_element(elements=users),
        )
        post_list.append(post)
    Post.objects.bulk_create(post_list)


def create_fake_comment():
    comment_num = Comment.objects.count()
    new_comment = 50 - comment_num
    comment_list = []
    users = list(CustomUser.objects.all())
    posts = list(Post.objects.all())

    for _ in range(new_comment):
        comment = Comment.objects.create(
            text=fake.text(max_nb_chars=150),
            author=fake.random_element(elements=users),
            post=fake.random_element(elements=posts),
        )
        comment_list.append(comment)
    Comment.objects.bulk_create(comment_list)
