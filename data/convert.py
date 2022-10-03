from utils import csv_to_json
import constants


if __name__ == '__main__':
    csv_to_json(constants.CSV_AD_PATH, constants.JSON_AD_PATH, 'ads.ad')
    csv_to_json(constants.CSV_CATEGORY_PATH, constants.JSON_CATEGORY_PATH, 'ads.category')
    csv_to_json(constants.CSV_LOCATION_PATH, constants.JSON_LOCATION_PATH, 'users.location')
    csv_to_json(constants.CSV_USER_PATH, constants.JSON_USER_PATH, 'users.user')
