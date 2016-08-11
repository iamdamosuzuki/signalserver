from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Configuration
from .models import Operation

from fileuploads.models import Result
from fileuploads.models import Row

from .forms import ConfigNameForm
from .forms import ConfigForm
from .forms import OperationForm


def index(request):
#     latest_config_list = Configuration.objects.order_by('-creation_date')[:5]
#     template = loader.get_template('operations/index.html')
#     context = {
#         'latest_config_list': latest_config_list,
#     }
#     return HttpResponse(template.render(context, request))
# def list(request):
#     # Handle file upload
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        config_name = request.POST['config_name']
        count = Configuration.objects.filter(
            configuration_name=config_name).count()
        display_order = request.POST['display_order']
        if form.is_valid() and count == 0:
            new_configuration = Configuration(
                configuration_name=config_name,
                display_order=display_order)
            new_configuration.save()
            return HttpResponseRedirect(
                reverse('operations:index'))

    return render_index(request)


def render_index(request):
    form = ConfigForm()  # A empty, unbound form
    # Load documents for the list page
    configurations = Configuration.objects.order_by('display_order')

    # Render list page with the documents and the form
    return render(request, 'operations/index.html',
                  {'configurations': configurations, 'form': form})


def delete_config(request, config_name):
    Configuration.objects.get(configuration_name=config_name).delete()
    return HttpResponseRedirect(reverse('operations:index'))


def delete_op(request, op_id, config_name):
    #configuration = Configuration.objects.get(configuration_name=config_name)
    #name = configuration
    Operation.objects.get(id=op_id).delete()
    return HttpResponseRedirect(reverse('operations:show',
                                kwargs={'config_name': config_name}))
    #form = OperationForm()
    #return render(request, 'operations/show.html',
    #              {'configuration': configuration, 'form': form})


def show(request, config_name):
    configuration = Configuration.objects.get(configuration_name=config_name)

    if request.method == 'POST':
        form = OperationForm(request.POST)
        cutoff_num = request.POST['cutoff_number']
        sig_name = request.POST['signal_fields']
        sig2_name = request.POST['second_signal_fields']
        op_name = request.POST['operation_fields']
        display_order = request.POST['display_order']
        if form.is_valid():
            new_operation = Operation(
                configuration=configuration,
                cut_off_number=cutoff_num,
                signal_name=sig_name,
                second_signal_name=sig2_name,
                op_name=op_name,
                display_order=display_order)
            new_operation.save()
            #return HttpResponseRedirect(
            #    reverse('operations:show'))

    #else:
    operation = Operation.objects.filter(
        configuration=configuration).order_by('display_order')
    form = OperationForm()  # A empty, unbound form
    #response = "resuot of configured operations %s."
    #return HttpResponse(response % config_name)
    return render(request, 'operations/show.html',
                  {'configuration': configuration,
                   'form': form, 'operation': operation})


def rename(request):
    if request.method == 'POST':
        old_name = request.POST['old_name']
        new_name = request.POST['new_name']
        configuration = Configuration.objects.filter(
            configuration_name=old_name)
        results = Result.objects.filter(config_name=old_name)
        for result in results:
            result.config_name = new_name
            result.save()
        for conf in configuration:
            conf.configuration_name = new_name
            conf.save()

    return HttpResponseRedirect(reverse('operations:index'))


def results(request, configuration_id):
    response = "resuot of configured operations %s."
    return HttpResponse(response % configuration_id)


def detail(request, configuration_id):
    try:
        operation = Operation.objects.get(pk=operation_id)
    except Operation.DoesNotExist:
        raise Http404("Operation does not exist")
    return render(request, 'operations/detail.html', {'operation': operation})
