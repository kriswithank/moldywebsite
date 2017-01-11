from django.shortcuts import render



def basicPage(request, template_name, additional_context):
    """
    Generates a basic page with the default header and footer. The active page is
    highlighted in the nav-menu based on the request path.

    Acts exactly like django.shortcuts.render but appends the nav_item_list to the context
    so that it dosn't have to be included multiple times.

    args:
        request - The standard HTTP request.
        template_name - The name of the template to render. The template should extend
                        common/base.html.
        context - Additional context for use in the template extension only. All context
                  required by base.html should already be inlcuded in this function.
    """
    context = {}
    context.update(additional_context)  # Add additional items.
    return render(request, template_name, context)
