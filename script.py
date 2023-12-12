class AlgoritmaLRU:

    def simulasi_LRU(self,references,frame):
        page_input = references
        frame_input = int(frame)
        pages = list(map(int, page_input.split()))
        simulation_result = self.cache_simulasi_LRU(pages, frame_input)
        return self.display_output(simulation_result, pages)


    def cache_simulasi_LRU(self,pages, cache_size):
        page_faults = 0
        cache = []
        simulation_steps = []

        def update_cache(page):
            nonlocal cache
            cache = [p for p in cache if p != page]
            cache.append(page)

        for page in pages:
            step = {
                'page': page,
                'cache_state': cache.copy(),
            }

            if page not in cache:
                page_faults += 1

                if len(cache) == cache_size:
                    cache.pop(0)
            else:
                update_cache(page)

            update_cache(page)

            simulation_steps.append(step)

        return {
            'page_faults': page_faults,
            'simulation_steps': simulation_steps,
        }


    def display_output(self,simulation_result, pages):
        page_faults = simulation_result['page_faults']
        simulation_steps = simulation_result['simulation_steps']

        total_references = len(pages)
        total_distinct_references = len(set(pages))
        hits = total_references - page_faults
        hit_rate = (hits / total_references) * 100
        fault_rate = (page_faults / total_references) * 100

        table_html = f"""Total References: {total_references}\nTotal Distinct References: {total_distinct_references}\nHits: {hits}\nFaults: {page_faults}\nHit Rate: {hit_rate:.2f}%\nFault Rate: {fault_rate:.2f}%
        """
        table_dict = {}

        for index, step in enumerate(simulation_steps):
            hit_or_miss = '✓' if self.cache_hit(pages, index, step['cache_state']) else '✗'
            table_dict[index + 1] = [step['page'], f"| {' | '.join(map(str, step['cache_state']))} |", hit_or_miss]
        return table_html,table_dict


    def cache_hit(self,pages, current_index, cache_state):
        current_reference = pages[current_index]
        return current_reference in cache_state