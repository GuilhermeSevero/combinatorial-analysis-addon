from typing import List, Union, TypedDict
import time


class ICombinationsValue(TypedDict):
    id: str
    value: float

class CombinationsUtil:
    @staticmethod
    def byValue(list_: List[ICombinationsValue], target: float, resolve_if_direct_match: bool = False) -> List[List[ICombinationsValue]]:
        inner_list = [{ 'id': el.get('id'), 'value': float(el.get('value')) } for el in list_]

        if resolve_if_direct_match:
            direct_matches = [el for el in inner_list if el.get('value') == target]

            if direct_matches:
                return [[el] for el in direct_matches]

        sorted_list = sorted(inner_list, key=lambda el: el.get('value'), reverse=True)
        combinations = CombinationsUtil.find_combination([], sorted_list, target)

        return [el for el in combinations if el]

    @staticmethod
    def find_combination(current: List[ICombinationsValue], remaining: List[ICombinationsValue], remaining_value: float) -> List[List[ICombinationsValue]]:
        if remaining_value == 0:
            return [current]

        if remaining_value < 0:
            return []

        inner_remaining = [el for el in remaining if el.get('value') <= remaining_value]
        if not inner_remaining:
            return []

        sum_of_remaining = round(sum(el.get('value') for el in inner_remaining), 2)
        if sum_of_remaining < remaining_value:
            return []

        invoice = inner_remaining[0]
        invoice_value = invoice.get('value')

        include_note = CombinationsUtil.find_combination(
            current + [invoice],
            inner_remaining[1:],
            round(remaining_value - invoice_value, 2),
        )

        exclude_note = CombinationsUtil.find_combination(
            current,
            inner_remaining[1:],
            remaining_value,
        )

        return include_note + exclude_note

if __name__ == '__main__':
    list_of_combinations: List[ICombinationsValue] = [
        { 'id': 'a23c00c6-3ff7-4f3b-872d-06e0f986c9a8', 'value': 8.04 },
        { 'id': '6743d757-209a-4a3d-b017-8b9dcf174dd9', 'value': 58.72 },
        { 'id': '76976296-1113-4b6c-ab86-7bca5969ffae', 'value': 3.54 },
        { 'id': 'ef7fd7b5-ddba-4592-9703-7c69baa64edf', 'value': 46.56 },
        { 'id': 'f486b486-ca17-4e86-a718-5e3c7b53bf00', 'value': 42.56 },
        { 'id': '9d0a270f-0198-45a1-a36b-80990231ed23', 'value': 15.84 },
        { 'id': '01077532-b232-4238-8008-b12a93adaa94', 'value': 4.46 },
        { 'id': 'db03157e-21e5-4f49-b494-ec4a89bd157b', 'value': 3.23 },
        { 'id': 'a025cd1c-d2d6-414e-b3de-3f698624c968', 'value': 12.56 },
        { 'id': '04516998-6cd3-497c-bed7-e6396de66291', 'value': 357.25 },
        { 'id': 'd2370a50-e03d-4a5a-9955-276d049943ab', 'value': 15.19 },
        { 'id': '5468e048-e14d-4e80-952d-ce6ad869cf42', 'value': 326.57 },
        { 'id': '8077b03f-d596-4a89-89de-4f55e0b5a505', 'value': 196.37 },
        { 'id': 'a51a70d0-1de1-4fec-b6e6-b47a6e90d74a', 'value': 11.47 },
        { 'id': '860f9ce6-399d-4fd5-a7f4-cad1fcaa4454', 'value': 270.96 },
        { 'id': 'ccc84420-215c-468e-80ef-f60a1093efcd', 'value': 450.62 },
        { 'id': '8983f97c-baaa-4ca7-9c2b-21106c6ae4af', 'value': 17.91 },
        { 'id': '25108789-2537-4b79-91f1-abe955bad49a', 'value': 162.98 },
        { 'id': '54484e2f-fb7c-43af-ab7e-5ec63c813ea8', 'value': 214.80 },
        { 'id': '87c8a386-e4f0-44a2-928c-4d9966a7779e', 'value': 129.21 },
        { 'id': '861dde67-925a-4a22-a001-e98b8d8e6fa3', 'value': 118.11 },
        { 'id': '0f0395b3-de45-48ce-97dc-cdff445248f4', 'value': 9.89 },
        { 'id': '4bc056b2-38dc-469d-b1a6-675da1b3c8d6', 'value': 24.71 },
        { 'id': '29ebd54d-11c6-4dac-9dcb-66ccc140e000', 'value': 19.59 },
        { 'id': 'bfc5769e-bb34-4e42-b4cb-cc151799eb0d', 'value': 8.66 },
        { 'id': '811c93d2-d467-46de-a64b-13514d04e637', 'value': 316.49 },
        { 'id': '8b67fb1d-c874-4724-a62e-0a7d0987d2e3', 'value': 7.91 },
        { 'id': '22d6801a-27cd-4750-8be3-c3f35fff1229', 'value': 10.92 },
        { 'id': 'c8e93189-54c8-4235-bd90-6cb418078cba', 'value': 10.82 },
        { 'id': '03adf52d-0e56-4b91-b27a-ddac8aa51ed0', 'value': 13.65 },
        { 'id': 'fba70572-1f6c-4b1a-9eef-006fed2778b1', 'value': 19.17 },
        { 'id': 'f5c26d01-cbd2-4995-8d9a-840bda4cb43e', 'value': 13.88 },
        { 'id': 'b94e4622-c746-466e-862c-842ac1e60946', 'value': 2116.48 },
        # { 'id': '2b649b8c-fecf-4e23-a744-8bf58426ab5f', 'value': 164.61 },
        # { 'id': '8d9ecc5a-7260-4187-ba79-1338e576cc33', 'value': 436.70 },
        # { 'id': 'de2cf79d-ab14-4e28-acc3-0a5915982f8e', 'value': 180.07 },
        # { 'id': 'aea65c1f-0bd2-4f16-b550-ce1946dc0a92', 'value': 2920.35 },
        # { 'id': '077b0482-c657-4336-9394-4f72228d95ee', 'value': 346.21 },
        # { 'id': '6324a973-74b1-47e7-9a02-10065b1882c0', 'value': 2315.22 },
        # { 'id': '7493e843-3499-4719-ac1e-5fbfe4393560', 'value': 227.13 },
    ]

    target_value = 2120.58
    resolve_direct_match = True

    util = CombinationsUtil()
    inicio = time.time()
    result = util.byValue(list_of_combinations, target_value, resolve_direct_match)
    fim = time.time()

    tempo_total = fim - inicio

    print(f"Tempo de execução: {tempo_total} segundos")
    print(f'Combinações encontradas: {len(result)}')

    # for combination in result:
    #     print('Combinação:', end=' ')
    #     for el in combination:
    #         print(f'\n    [{el.get("id")}, {el.get("value")}]', end=' ')
    #     print()