openerp.test_module = function(instance, local) {

  local.TestWidget = instance.Widget.extend({
    start: function() {
      console.log('Widget loaded!');
      this._super();
    },
  });

  instance.web.client_actions.add('example.action', 'instance.test_module.TestWidget');
}
