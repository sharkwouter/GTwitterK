import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2


@Gtk.Template.from_file("window.ui")
class Window(Gtk.ApplicationWindow):
    # Load the Window class from the ui file
    __gtype_name__ = "Window"

    # Load widgets from ui file
    button_back = Gtk.Template.Child()
    button_forward = Gtk.Template.Child()
    webview_container = Gtk.Template.Child()

    def __init__(self, name="GTwitterK"):
        Gtk.ApplicationWindow.__init__(self, title=name)

        # Create webview which will show twitter
        context = WebKit2.WebContext.new()
        self.webview = WebKit2.WebView.new_with_context(context)

        # Set persistent cookies
        self.cookie_manager = context.get_cookie_manager()
        self.cookie_manager.set_persistent_storage(".cache", WebKit2.CookiePersistentStorage.SQLITE)

        self.webview.load_uri("https://mobile.twitter.com/")

        self.webview_container.add(self.webview)
        self.show_all()

    @Gtk.Template.Callback("on_button_back_clicked")
    def back(self, widget):
        self.webview.go_back()

    @Gtk.Template.Callback("on_button_forward_clicked")
    def forward(self, widget):
        self.webview.go_forward()

    @Gtk.Template.Callback("on_button_compose_clicked")
    def compose(self, widget):
        self.webview.load_uri("https://mobile.twitter.com/compose/tweet")

