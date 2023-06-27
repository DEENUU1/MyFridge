from faker import factory, Faker
from users.models import CustomUser, UserFollowing

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
