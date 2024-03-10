module Jekyll
  class LiquidVersionTag < Liquid::Tag
    def render(context)
      Liquid::VERSION
    end
  end
end

Liquid::Template.register_tag('liquid_version', Jekyll::LiquidVersionTag)
