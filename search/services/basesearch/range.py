
from search.common.utils import stupid_count_tokens
import pandas as pd


from search.common import structures


def _build_tokens_count(data_source, search_text):
    tokens = search_text.split()
    res = data_source['document'].apply(lambda x: stupid_count_tokens(tokens, x))
    res.name = None
    return res


def _get_gender_mask(data_source: pd.DataFrame, user_data: structures.User):
    return data_source['gender'].apply(lambda x: stupid_count_tokens([user_data.gender], x))


def _get_age_mask(data_source: pd.DataFrame, user_data: structures.User):
    return data_source.apply(lambda x: x['age_from'] <= user_data.age <= x['age_to'], axis=1)


def _sort_by_rating_and_tokens(rating, tokens_count, key_md5):
    df = pd.concat([tokens_count, rating, key_md5], axis=1)
    return df.sort_values([0, 1, 'key_md5'], ascending=[False, False, False])


def range_sort(data_source: pd.DataFrame, request: structures.BaseSearchRequest):
    tokens_count = _build_tokens_count(data_source, request.search_text)
    gender_mask = _get_gender_mask(data_source, request.user_data)
    age_mask = _get_age_mask(data_source, request.user_data)
    rating = gender_mask + age_mask

    df = _sort_by_rating_and_tokens(rating, tokens_count, data_source['key_md5'])
    return {'documents': data_source.loc[df.head(request.limit).index].to_dict('records')}