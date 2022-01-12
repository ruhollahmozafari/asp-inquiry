from rest_framework.filters import rest_filters
from .models.device_models import Device




class PhonesFilterSet(rest_filters.FilterSet):
    brands = InListFilter(field_name='brand__id')
    os_ids = InListFilter(field_name='versions__os')
    version_ids = InListFilter(field_name='versions')
    launched_year_gte = rest_filters.NumberFilter(field_name='phone_launched_date__year', lookup_expr='gte')
    ram_gte = rest_filters.NumberFilter(field_name='internal_memories__value', method='get_rams')
    ram_memory_unit = rest_filters.NumberFilter(field_name='internal_memories__units', method='get_ram_units')

    def get_rams(self, queryset, name, value):
        #here is the problem filter
        #that not works with ordering by name
        q=queryset.filter(Q(internal_memories__memory_type=1) & Q(internal_memories__value__gte=value))
        print('filter_set', len(q))
        print('filter_set_query', q.query)
        return q


    def get_ram_units(self, queryset, name, value):
        return queryset.filter(Q(internal_memories__memory_type=1) & Q(internal_memories__units=value))


    class Meta:
        model = Device
        fields = ['brands', 'os_ids', 'version_ids', 'status', 'ram_gte']





class CustomFilterBackend(filters.OrderingFilter):
    allowed_custom_filters = ['ram', 'camera', 'year']

    def get_ordering(self, request, queryset, view):
        params = request.query_params.get(self.ordering_param)

        if params:
            fields = [param.strip() for param in params.split(',')]
            ordering = [f for f in fields if f in self.allowed_custom_filters]
            if ordering:
                return ordering

        # No ordering was included, or all the ordering fields were invalid

        return self.get_default_ordering(view)


    def filter_queryset(self, request, queryset, view):
        ordering = self.get_ordering(request, queryset, view)
        if ordering:
            if 'ram' in ordering:
                max_ram = Max('internal_memories__value', filter=Q(internal_memories__memory_type=1))
                queryset = queryset.annotate(max_ram=max_ram).order_by('-max_ram')
            elif 'camera' in ordering:
                max_camera = Max('camera_pixels__megapixels', filter=Q(camera_pixels__camera_type=0))    
                queryset = queryset.annotate(max_camera=max_camera).order_by('-max_camera')            
            elif 'year' in ordering:
                queryset = queryset.filter(~Q(phone_released_date=None)).order_by('-phone_released_date__year')
            elif 'name' in ordering:
                #here is the problem ordering
                #thats not working with filter
                #with one to many relations
                queryset = queryset.order_by('-brand__name', '-model__name')


        return queryset