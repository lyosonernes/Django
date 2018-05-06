# coding: utf-8
from __future__ import unicode_literals

import django_tables2 as tables

from .models import Country, Person

from django.utils.safestring import mark_safe
from django.utils.html import escape



class MyColumn(tables.Column): 
    empty_values = list() 
    def render(self, value, record):
        return mark_safe('<button id="%s" value="specs" class="btn btn-default">Specs</button>' % escape(record['id']))
		
class MyColumn2(tables.Column): 
    empty_values = list() 
    def render(self, value, record):
        return mark_safe('<button id="%s" value="edit" class="btn btn-default">Edit</button>' % escape(record.name))

class CountryTable(tables.Table):
    name = tables.Column()
    population = tables.Column()
    tz = tables.Column(verbose_name='time zone')
    visits = tables.Column()
    summary = tables.Column(order_by=('name', 'population'))
    submit = MyColumn()
	
    class Meta:
        model = Country


class ThemedCountryTable(CountryTable):
    class Meta:
        attrs = {'class': 'paleblue'}


class BootstrapTable(tables.Table):

    # country = tables.RelatedLinkColumn()
    # continent = tables.Column(accessor='country.continent.name', verbose_name='Continent')
    name = tables.Column()
    specs = MyColumn(orderable=False)
    # edit = MyColumn2()
	
    class Meta:
        # model = Person
        template_name = 'django_tables2/bootstrap.html'
        # exclude = ('friendly', )
        attrs = {'class': 'table table-hover'}

class BootstrapTablePinnedRows(BootstrapTable):

    # class Meta(BootstrapTable.Meta):
        # pinned_row_attrs = {
            # 'class': 'info'
        # }

    def get_top_pinned_data(self):
        return [
            {'name': 'Most used country: ', 'country': Country.objects.filter(name='Cameroon').first()}
        ]


class Bootstrap4Table(tables.Table):
    country = tables.RelatedLinkColumn()
    # continent = tables.RelatedLinkColumn(accessor='country.continent')

    class Meta:
        model = Person
        template_name = 'django_tables2/bootstrap4.html'
        attrs = {'class': 'table table-hover'}
        exclude = ('friendly', )


class SemanticTable(tables.Table):

    country = tables.RelatedLinkColumn()

    class Meta:
        model = Person
        template_name = 'django_tables2/semantic.html'
        exclude = ('friendly', )


class PersonTable(tables.Table):
    country = tables.RelatedLinkColumn()

    class Meta:
        model = Person
        template_name = 'django_tables2/bootstrap.html'
