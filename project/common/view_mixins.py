from django.contrib.auth import mixins
from django.http import Http404
from django.shortcuts import redirect


class RedirectToDashboard:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("logged")

        return super().dispatch(request, *args, **kwargs)


class TheCreatorPermissionMixin(mixins.UserPassesTestMixin):
    def test_func(self):
        return self.get_object().user_id == self.request.user.id


# class SameUserOnlyMixin(object):
#
#     def has_permissions(self):
#         # Assumes that your Article model has a foreign key called `auteur`.
#         return self.get_object().auteur == self.request.user
#
#     def dispatch(self, request, *args, **kwargs):
#         if not self.has_permissions():
#             raise Http404('You do not have permission.')
#         return super(SameUserOnlyMixin, self).dispatch(
#             request, *args, **kwargs)
